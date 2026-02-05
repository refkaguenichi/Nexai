import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors({
  origin: '*'  // allow all for now
});
  const port = process.env.PORT ?? 5000
  await app.listen(port, () => {
      console.log(
        `🚀 MS is running on port ${port}`,
      );
    });
}
bootstrap();
